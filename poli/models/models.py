"""
    This file is part of Polichombr.

    (c) 2016 ANSSI-FR


    Description:
        Generic models.
"""


class CustomEnum(object):

    """
        Utility class to implement a int/str enum
    """
    @classmethod
    def tostring(cls, val):
        for key, value in vars(cls).iteritems():
            if value == val:
                return key
        return ""

    @classmethod
    def fromstring(cls, val):
        return getattr(cls, val, None)


class TLPLevel(CustomEnum):

    """
    TLP sensibility level. https://www.us-cert.gov/tlp
    BLACK level: "Keep the information private", should not be exported.
    """
    (
        TLPWHITE,
        TLPGREEN,
        TLPAMBER,
        TLPRED,
        TLPBLACK
    ) = range(1, 6)


TLPLevelChoices = [
    (TLPLevel.TLPWHITE, 'TLP White'),
    (TLPLevel.TLPGREEN, 'TLP Green'),
    (TLPLevel.TLPAMBER, 'TLP Amber'),
    (TLPLevel.TLPRED, 'TLP Red'),
    (TLPLevel.TLPBLACK, 'TLP Black')]
