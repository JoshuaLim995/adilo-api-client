import dataclasses
import json
from typing import Optional


@dataclasses.dataclass
class Project:
    id: str
    title: str
    description: str
    private: bool
    archived: bool
    drm: bool
    locked: bool
    created_at: str
    updated_at: str


@dataclasses.dataclass
class ProjectList:
    projects: list[Project]
    total: int
    from_: int
    to: int


@dataclasses.dataclass
class Folder:
    id: str
    name: str
    project: Project | dict | None = None
    project_id: str = dataclasses.field(init=False)
    parent_folder: "Folder | dict | None" = None
    parent_folder_id: str = dataclasses.field(init=False)

    def __post_init__(self):
        if self.project and isinstance(self.project, dict):
            self.project = Project(**self.project)
            self.project_id = self.project.id
        if self.parent_folder and isinstance(self.parent_folder, dict):
            self.parent_folder = Folder(**self.parent_folder)
            self.parent_folder_id = self.parent_folder.id


@dataclasses.dataclass
class FolderList:
    folders: list[Folder]
    total: int
    from_: int
    to: int


@dataclasses.dataclass
class Part:
    part_number: int
    etag: str

    def to_dict(self):
        return {
            "PartNumber": self.part_number,
            "ETag": self.etag,
        }

    def to_json(self):
        return json.dumps(self.to_dict())


@dataclasses.dataclass
class InitiateUpload:
    upload_id: str
    key: str

    @classmethod
    def from_dict(cls, data: dict) -> "InitiateUpload":
        data_upload_id = data.get("uploadId")
        data_key = data.get("key")

        assert data_upload_id is not None, "uploadId is required"
        assert data_key is not None, "key is required"

        return cls(
            upload_id=data_upload_id,
            key=data_key,
        )


@dataclasses.dataclass
class SignedUpload:
    method: str
    url: str
