# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project State

Claude Code 配置和命令仓库。包含自定义 slash 命令和中文文档翻译工作流。

## 已实现的自定义命令

| 命令 | 文件 | 用途 |
|------|------|------|
| `/commit` | `.claude/commands/commit.md` | 使用约定式提交格式和 emoji 创建提交 |
| `/transfer` | `.claude/commands/transfer.md` | 将 Markdown 文件翻译为中文并输出到 `output/` |
| `/create-pr` | `.claude/commands/create-pr.md` | 创建新分支、提交更改并提交 PR |
| `/clean` | `.claude/commands/clean.md` | 修复整个代码库的 black、isort、flake8、mypy 问题 |
| `/update-docs` | `.claude/commands/update-docs.md` | 更新实现文档 |
| `/add-to-changelog` | `.claude/commands/add-to-changelog.md` | 更新变更日志 |

## 翻译工作流

- 使用 `/transfer <文件名.md>` 将命令文档翻译为中文
- 翻译输出保存在 `output/` 目录
- 翻译保留原文件结构、emoji 和代码块

## 目录结构

```
.claude/commands/   - 自定义 slash 命令定义（Markdown 格式）
output/             - 中文翻译输出文件
CLAUDE.md           - 项目指导文件
README.md           - 项目说明
