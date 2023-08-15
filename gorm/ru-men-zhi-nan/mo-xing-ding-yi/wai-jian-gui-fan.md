gorm外键的规范性写法示例:

```go
type DtProject struct {
	gorm.Model
	Name  string `json:"name" form:"name" gorm:"column:name;comment:;type:varchar(191);"`
}

type DtProjectWorkerRel struct {
	gorm.Model
	ProjectId    uint   `json:"projectId" gorm:"comment:项目id;unique_index:project_company_idcard_idx"`
	Project DtProject `gorm:"foreignKey:ID;references:ProjectId;"`
	}

```

`gorm:"foreignKey:关联表的结构体字段;references:当前表的结构体字段;`

报错处理: define a valid foreign key for relations or implement the Valuer/Scanner interface

```go
type UpLoadFile struct {
	gorm.Model
	FileName    string    `json:"file_name" gorm:"comment:文件名"`
	FileChunk   []FileChunk `json:"file_chunk" gorm:"-"`
}

type FileChunk struct {
	gorm.Model
	FileId          uint
	FileChunkNumber int
	FileChunkPath   string
}

```

