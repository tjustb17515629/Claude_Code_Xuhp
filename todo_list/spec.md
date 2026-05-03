# 待办事项 Web 应用 — 实现规格

## 概述

基于 Django 的待办事项 Web 应用，个人使用，支持任务增删改查、分类筛选和数据统计。

## 技术栈

| 层 | 选型 |
|------|------|
| 后端框架 | Django 4.x |
| 数据库 | SQLite |
| 前端 | Django 模板 + 少量 JS |
| 样式 | 纯 CSS |

## 数据模型

```python
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    category = models.CharField(
        max_length=20,
        choices=[
            ('study', '学习'),
            ('entertainment', '娱乐'),
            ('work', '工作'),
            ('life', '生活'),
        ],
        default='study',
    )
    due_date = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | CharField(200) | 任务标题 |
| `completed` | BooleanField | 完成状态 |
| `category` | CharField | 类型：学习/娱乐/工作/生活 |
| `due_date` | DateField | 截止日期（可选） |
| `tags` | CharField | 标签，逗号分隔（可选） |
| `created_at` | DateTimeField | 创建时间（自动） |
| `updated_at` | DateTimeField | 更新时间（自动） |

## URL 设计

| 方法 | URL | 功能 |
|------|-----|------|
| GET | `/` | 任务列表，支持 `?filter=active\|completed` 和 `?category=study\|entertainment\|work\|life` |
| POST | `/add/` | 新增任务 |
| POST | `/toggle/<id>/` | 切换完成状态 |
| POST | `/delete/<id>/` | 删除任务 |
| GET | `/edit/<id>/` | 编辑任务页面 |
| POST | `/edit/<id>/` | 保存编辑 |

## 页面清单

### 1. 列表页（首页 `/`）

- 顶部：任务统计（总计/进行中/已完成）
- 筛选栏：全部 | 进行中 | 已完成，按类型筛选
- 新增区域：输入框 + 类型选择 + 截止日期 + 标签 + 添加按钮
- 任务列表：标题、类型标签、截止日期、完成勾选框、编辑/删除按钮
- 已完成任务显示删除线

### 2. 编辑页（`/edit/<id>/`）

- 表单：标题、类型、截止日期、标签、完成状态
- 保存按钮 + 返回链接

### 3. 统计页（后续阶段）

- 各类型任务数量/完成率
- 简单图表

## 项目结构

```
todo_list/
├── manage.py
├── db.sqlite3
├── todo_app/              # Django 项目
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo/                  # Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/todo/
│       ├── base.html
│       ├── list.html
│       └── edit.html
└── static/
    └── style.css
```

## 功能阶段

### Phase 1 ✅ 当前

- [ ] Django 项目初始化
- [ ] 数据模型 + 迁移
- [ ] 任务列表页（含筛选）
- [ ] 新增任务
- [ ] 编辑任务
- [ ] 删除任务
- [ ] 标记完成/取消
- [ ] 基本样式

### Phase 2 ⬜ 后续

- [ ] 统计页面
- [ ] 批量操作
- [ ] 搜索功能
- [ ] 响应式移动端适配
