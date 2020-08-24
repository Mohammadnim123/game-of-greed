from tests.flow.flo import Flo

def test_quitter():
    Flo.test("tests/flow/quitter.txt")

def test_wanna_play_then_quit():
    Flo.test("tests/flow/do_wanna_play_then_quit.txt")
