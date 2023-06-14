import nox


@nox.session(python=["3.6", "3.7", "3.8", "3.9"])
def multi_version(session):
    pass


@nox.session(python="3.9")
def single_version(session):
    pass


@nox.session(python="3.9")
@nox.parametrize("param", ["a", "b", "c"])
def parametrized(session, param):
    pass


@nox.session(python="3.9")
@nox.parametrize("param", ["1", "2", "3"], ids=["one", "two", "three"])
def parametrized_display_name(session, param):
    pass


@nox.session(python="3.9")
def ignored(session):
    pass


@nox.session(python="3.9", name="custom_name")
def renamed(session):
    pass
