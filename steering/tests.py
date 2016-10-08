import os
import keras
import tensorflow

SAMPLE_DATA='/data/data/sample.bag'


def test_versions():
    """Check we can load tensorflow and keras.
    """
    assert tensorflow.__version__ is not None
    assert keras.__version__ is not None


def test_sample_data():
    """Make sure sample bag file is accesible
    """
    assert os.path.isfile(SAMPLE_DATA)
