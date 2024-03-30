from streamlit.testing.v1 import AppTest

def test_default():
    assert 5==5

def test_session_variable():
    at = AppTest.from_file("app.py")
    at.run(timeout=30)
    assert at.session_state['upload'] == False

def test_loading_page():
    at = AppTest.from_file("app.py")
    at.session_state.login="success"
    at.run(timeout=10)
    assert at.subheader[0].value=='AI-Powered Audio Summarization Tool'

def test_make_prompt():
    def script():
        import app
        app.make_prompt("Testing")
    at = AppTest.from_function(script)
    at.run(timeout=10)
    assert not at.exception

def test_radio_option():
    at = AppTest.from_file("app.py")
    at.run(timeout=10)
    at.radio[0].set_value("Live Recording")
    assert at.session_state['live'] == True

def test_generate_summary():
    at = AppTest.from_file("app.py")
    at.run(timeout=10)
    at.button[0].click().run()
    assert at.error[0].value=="Please add your audio."