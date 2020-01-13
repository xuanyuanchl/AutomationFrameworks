

class angular_is_ready(object):
    """taken from http://stackoverflow.com/a/33378576"""
    
    script = """var callback = arguments[arguments.length - 1];
    var el = document.querySelector('html');
    if (!window.angular) {
        callback('False')
    }
    if (angular.getTestability) {
        angular.getTestability(el).whenStable(function(){callback('True')});
    } else {
        if (!angular.element(el).injector()) {
            callback('False')
        }
        var browser = angular.element(el).injector().get('$browser');
        browser.notifyWhenNoOutstandingRequests(function(){callback('True')});
    };"""

    def __call__(self, driver):
        try:
            return driver.execute_async_script(self.script)
        except:
            return False
