import pytest
import data
from Library import Library


def test_upload_in_naukri():

    with Library() as obj:
        result = obj.upload_resume_to_naukri(data.naukri_username, data.naukri_password)
        assert result, "Upload in Naukri Failed"
    # a = Library()
    # a.upload_resume_to_naukri(data.naukri_username, data.naukri_password)