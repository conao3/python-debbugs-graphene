from datetime import datetime
import enum
from typing import Any, Optional
import pydantic


class BugPendingEnum(str, enum.Enum):
    PENDING = "pending"
    DONE = "done"


class Bug(pydantic.BaseModel):
    bug_num: int  # Integer The bugnumber
    subject: Optional[str] = None  # String Subject/Title of the bugreport
    summary: Optional[str] = None  # String Arbitrary text

    originator: Optional[str] = None  # String Submitter of the bugreport
    owner: Optional[str] = None  # String default: empty, otherwise: who is responsible for fixing
    done: Optional[str] = None  # String Maintainer who closed the bug, or empty string if it's not closed

    blocks: Optional[str] = None  # List of Integers [*] Bugreports this bug blocks
    blockedby: Optional[str] = None  # List of Integers [*] Bugreports this bug is blocked by
    severity: Optional[str] = None  # String Severity of the bugreport
    affects: Optional[str] = None  # List of Strings Packagenames, see 'affects'-field in control-BTS manual
    package: Optional[str] = None  # String Package of the Bugreport
    tags: Optional[list[str]] = None  # split ' '  # List of Strings Tags of the bugreport
    source: Optional[str] = None  # String Source package of the Bugreport
    archived: Optional[bool] = None  # convert from int  # Boolean The bug is archived or not
    fixed_versions: Optional[list[str]] = None  # List of Strings Version Numbers, can be empty even if the bug is fixed
    found_versions: Optional[list[str]] = None  # List of Strings Version Numbers
    forwarded: Optional[str] = None  # String some URL, sometimes an email address
    pending: Optional[BugPendingEnum] = None  # String Either 'pending' or 'done'
    msgid: Optional[str] = None  # String Message ID of the bugreport
    location: Optional[str] = None  # String Always 'db-h' or 'archive'

    date: Optional[datetime] = None  # convert from int  # DateTime Date of bug creation
    mergedwith: Optional[list[int]] = None  # split ' '  # List of Integers [*] The bugs this bug was merged with
    unarchived: Optional[int] = None  # convert from int  # Boolean Has the bug been unarchived and can be archived again
    log_modified: Optional[datetime] = None  # convert from int  # DateTime Date of last update
    last_modified: Optional[datetime] = None  # convert from int  # DateTime Date of last update

    # deprecated fields

    # keywords: Any = None  # List of Strings Copy of 'tags'
    # fixed_date: Any = None  # DateTime empty for now
    # found_date: Any = None  # DateTime empty for now
    # id: Any = None  # Integer Will vanish in future versions, use bug_num
    # found: Any = None  # Dict Not fully implemented in debbugs, use found_versions for now
    # fixed: Any = None  # Dict Not fully implemented in debbugs, use fixed_versions for now
