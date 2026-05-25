## 项目 1：CSV 学员数据分析器

- 读取一个学员 CSV 文件（含姓名、邮箱、加入日期、所在国家、对赌状态）
- 统计：总人数、各国家人数、对赌完成率
- 把统计结果保存为 `report.json`

## 项目 2：JSON 配置文件读写器

- 读取一个 `config.json`（含用户偏好设置，如主题、语言、字体大小）
- 命令行让用户修改任意一个设置
- 修改后保存回 `config.json`

## 项目 3：带单元测试的字符串工具库

- 写一个 `string_utils.py`，包含 3 个函数：
  - `reverse_words(s)`：反转单词顺序（`"hello world"` → `"world hello"`）
  - `count_vowels(s)`：统计元音字母数量
  - `is_palindrome(s)`：判断是否回文
- 写一个 `test_string_utils.py`，用 `pytest` 测试上面 3 个函数
- 每个函数至少 3 个测试用例（含正常情况、边界情况、异常情况）
- 在终端运行 `pytest` 确认所有测试通过
