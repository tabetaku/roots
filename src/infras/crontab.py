import json
import os
import subprocess

from requests import get
from uwsgidecorators import timer


# NAS 에서 자동 업데이트를 위한 기능
# NAS Docker 에 자동 재시작 설정함
# Docker 가 뜨면서 현재 commit 의 HASH 데이터를 떨꾸고 Master 의 최신 파일 가져옴
# 새로운 hash 가 있는지 계속 검사하고 있으면 uwsgi 를 kil 함
# Docker 가 재시작하면서 Master 의 최신 파일 가져옴
@timer(10)
def self_kill_if_update_available(signum: int):
    # 일단 하드코딩으로 작성한다.
    work_dir = os.environ['WORK_DIR']

    # Step 1. Local hash json 읽기
    with open(f'{work_dir}/hash.txt') as json_file:
        local_data = json.load(json_file)
    local_hash = local_data['commit']['sha']

    # Step 2. 현재 github hash json 가져오기
    github_repo = os.environ['GITHUB_REPO']
    github_owner = os.environ['GITHUB_OWNER']
    github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
    url = f'https://api.github.com/repos/{github_owner}/{github_repo}/branches/master'

    headers = {'Authorization': f'token {github_access_token}', 'Accept': 'application/vnd.github.v3+json'}
    res = get(url, headers=headers)
    current_hash = res.json()
    current_hash = current_hash['commit']['sha']

    # Step 3. 새버전이 없으면 아무일도 하지 않는다.
    if local_hash == current_hash:
        return

    # Step 4. 새로운 버젼이 나왔으면 uwsgi 종료!
    subprocess.call('pkill -f uwsgi -9', shell=True)
