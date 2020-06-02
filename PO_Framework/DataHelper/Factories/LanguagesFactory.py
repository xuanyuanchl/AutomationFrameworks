
from DataHelper.Models.Languages import Languages
from DataHelper.EOLDBAccess import dbAccess

def Create(languageIncId, languageSqlId, languageCode,
           languageName, isDeleted, isSupported, isoLanguageCode, translationTag):

    languages = Languages()

    languages.languageIncId = languageIncId
    languages.languageSqlId = languageSqlId
    languages.languageCode = languageCode
    languages.languageName = languageName
    languages.isDeleted = isDeleted
    languages.isSupported = isSupported
    languages.isoLanguageCode = isoLanguageCode
    languages.translationTag = translationTag

    return dbAccess.dbSession.add(languages)
