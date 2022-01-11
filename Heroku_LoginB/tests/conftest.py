import pytest

from . import config

def pytest_addoption(parser):
    parser.addoption('--baseurl',
                     action='store',
                     default='https://the-internet.herokuapp.com',
                     help='endereço do site alvo do teste'
    )
    parser.addoption('--host',
                     action='store',
                     default='saucelabs',
                     help='ambiente em que vou executar os testes'
    )
    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='navegador padrão'
    )
    parser.addoption('--browserversion',
                     action='store',
                     default='97.0.4692.71',
                     help='versão navegador padrão97.0.4692.71'
    )
    parser.addoption('--platform',
                     action='store',
                     default='Windows 10',
                     help='Sistema operacional'
    )

@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.browser = request.config.getoption('--browser')
    config.browserVersion = request.config.getoption('--browserVersion')
    config.platform = request.config.getoption('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name # adicionar o nome de teste baseado no script
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce.options': {
                'name': test_name,
            }
        }
        #ToDo: _credentials =