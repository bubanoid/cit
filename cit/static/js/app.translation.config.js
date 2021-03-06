app.config(function ($translateProvider) {

    var language = (window.navigator.languages)[0];
    var userLanguage;

        if (language.length >2) {
            userLanguage = language.slice(0,2)
        } else {userLanguage = language}

  $translateProvider.translations('uk', {
    SIGN_IN_WITH_FACEBOOK: 'Увійти через Facebook',
    LOGOUT: 'Вийти',
    HOME: 'Головна',
    LOGO: 'Логотип',
    WARNING: 'Увага',
	PROFILE: 'Профіль'
  });
   $translateProvider.translations('en', {
    SIGN_IN_WITH_FACEBOOK: 'Sign in with Facebook',
    LOGOUT: 'Logout',
    HOME: 'Home',
    LOGO: 'Logo',
    WARNING: 'Warning',
	PROFILE: 'Profile'
  });
  $translateProvider.translations('ru', {
    SIGN_IN_WITH_FACEBOOK: 'Ввойти через Facebook',
    LOGOUT: 'Выйти',
    HOME: 'Главная',
    LOGO: 'Логотип',
    WARNING: 'Внимание',
	PROFILE: 'Профиль'
  });
  $translateProvider.preferredLanguage(userLanguage);
 });

