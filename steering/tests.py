
# content of test_sample.py
def test_imports():
    """Check we can load tensorflow and keras.
    """
    import tensorflow
    import keras

    assert tensorflow.__version__ is not None
    assert keras.__version__ is not None
