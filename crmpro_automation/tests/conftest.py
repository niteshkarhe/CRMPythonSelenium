import traceback
import pytest
from PyTestFramework.crmpro_automation.base.drivermanagerfactory import DriverManagerFactory
from PyTestFramework.crmpro_automation.filereader.environment_reader import EnvironmentReader
from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture
from PyTestFramework.crmpro_automation.configfiles.manage_report import ManageReport

@pytest.fixture(scope="class")
def setUp(request):
    try:
        driver=DriverManagerFactory.get_manager(EnvironmentReader().get_environment_dict().get('BrowserName'))
        environment=EnvironmentReader().get_environment_dict()
        #driver.get_driver()
        # add `driver` attribute to the class under test
        if request.cls is not None:
                request.cls.driver = driver 
                request.cls.environment = environment
        yield driver, environment
        report_path_details=BaseFixture.report_folder_file_path()
        ManageReport().write_report_path(report_path_details)
        BaseFixture.log.info('Report file path and assets folder path is updated in report_resources.txt')
        request.cls.driver.stop_service()
        BaseFixture.log.info('ChromeDriver Service is stopped and Browser is closed.')
    except:
        print(traceback.print_exc())

        
''' ### To attach screenshot to html report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
 
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            BaseFixture().screenshot(False, "failure")
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra '''