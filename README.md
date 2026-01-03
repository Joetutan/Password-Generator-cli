




```bash
$ pwdgen init

$ pwdgen add github.com  --length 20 --charset base64
# Account (name: github.com) added successfully!

$ pwdgen add gmail.com --length 16 --charset alnum
# Account (name: gmail.com) added successfully!

$ pwdgen get github.com
$ Enter master password:
# Account: github.com password: generatedpass

$ pwdgen rotate github.com
# Expense added successfully (ID: 2)

$ pwdgen list
# Expense added successfully (ID: 2)

```