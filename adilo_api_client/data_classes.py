import dataclasses
import json


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
        return dataclasses.asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict())
