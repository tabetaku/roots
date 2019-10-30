from libs.base.constants import BaseConstant


class GenderType(BaseConstant):
    MAN = 0
    WOMAN = 1

    OTHER = 65535

    _LIST = (MAN, WOMAN, OTHER,)
    _STRING_MAP = {
        MAN: '남자',
        WOMAN: '여자',
        OTHER: '기타',
    }

    _PARAM_MAP = {
        MAN: 'man',
        WOMAN: 'woman',
        OTHER: 'other',
    }


class ContentType(BaseConstant):
    MOVIE = 0
    JP_DRAMA = 1

    _LIST = (MOVIE, JP_DRAMA,)
    _STRING_MAP = {
        MOVIE: '영화',
        JP_DRAMA: '일본드라마',
    }

    _PARAM_MAP = {
        MOVIE: 'movie',
        JP_DRAMA: 'jp_drama',
    }


class ParticipantType(BaseConstant):
    LEAD_ACTOR = 0
    SUPPORTING_ACTOR = 1
    PRODUCTION = 2
    DIRECTOR = 3
    AUTHOR = 4

    _LIST = (LEAD_ACTOR, SUPPORTING_ACTOR, PRODUCTION, DIRECTOR, AUTHOR,)
    _STRING_MAP = {
        LEAD_ACTOR: '주연',
        SUPPORTING_ACTOR: '조연',
        PRODUCTION: '연출',
        DIRECTOR: '감독',
        AUTHOR: '작가',
    }

    _PARAM_MAP = {
        LEAD_ACTOR: 'lead_actor',
        SUPPORTING_ACTOR: 'supporting_actor',
        PRODUCTION: 'production',
        DIRECTOR: 'director',
        AUTHOR: 'author',
    }
