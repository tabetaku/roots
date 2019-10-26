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
