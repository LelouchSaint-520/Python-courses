核心配置：设置用户名和邮箱
打开您的终端（Terminal、Git Bash、CMD 或 PowerShell），然后输入以下两条命令，请将引号内的内容替换为您自己的信息。

1. **设置您的用户名：** 这个名字将会出现在您所有的提交记录中。
    
    Bash
    
    ```
    git config --global user.name "Your Name"
    ```
    
    - 例如：`git config --global user.name "Zhang San"`
        
2. **设置您的邮箱地址：** 这个邮箱地址也会与您的提交记录关联，建议使用您在 GitHub/GitLab 等代码托管平台上注册的邮箱。
    
    Bash
    
    ```
    git config --global user.email "your.email@example.com"
    ```
    
    - 例如：`git config --global user.email "zhangsan@gmail.com"`
        

完成这两步后，您最基本的全局配置就已经初始化好了。

---

### 查看配置

如果您想检查您的配置是否成功，可以使用以下命令：

1. **查看所有全局配置：**
    
    Bash
    
    ```
    git config --global --list
    ```
    
    您应该能看到刚刚设置的 `user.name` 和 `user.email`。
    
2. **查看某个特定的配置项：**
    
    Bash
    
    ```
    git config --global user.name
    git config --global user.email
    ```
    

### 其他推荐的全局配置

除了用户名和邮箱，还有一些非常有用的全局配置可以提升您的使用体验。

1. **设置默认分支名（推荐）：** 传统上 Git 的默认主分支是 `master`，但现在社区更推荐使用 `main`。您可以通过以下命令设置未来所有 `git init` 创建的新仓库都使用 `main` 作为默认分支。
    
    Bash
    
    ```
    git config --global init.defaultBranch main
    ```
    
2. **设置默认的文本编辑器：** 当 Git 需要您输入信息时（例如，编写提交信息），它会调用一个文本编辑器。您可以设置为您习惯的编辑器，如 VS Code, Vim, Sublime Text 等。
    
    Bash
    
    ```
    # 设置为 Visual Studio Code (推荐，--wait 参数很关键)
    git config --global core.editor "code --wait"
    
    # 设置为 Sublime Text
    # git config --global core.editor "subl -n -w"
    
    # 设置为 Vim (通常是类 Unix 系统的默认值)
    # git config --global core.editor "vim"
    ```
    
3. **启用命令着色：** 让 Git 的输出在终端中以不同颜色显示，更加清晰易读。
    
    Bash
    
    ```
    git config --global color.ui auto
    ```
    
4. **创建命令别名（Alias）：** 为常用的、冗长的命令创建简短的别名，可以极大提高效率。
    
    Bash
    
    ```
    # st 代替 status
    git config --global alias.st status
    
    # co 代替 checkout
    git config --global alias.co checkout
    
    # br 代替 branch
    git config --global alias.br branch
    
    # ci 代替 commit
    git config --global alias.ci commit
    
    # 创建一个更漂亮的 log 命令 lg
    git config --global alias.lg "log --oneline --graph --decorate --all"
    ```
    
    设置好后，您就可以用 `git st` 来代替 `git status`，用 `git lg` 查看简洁的提交历史图。
    

### 配置文件在哪里？

所有使用 `--global` 标志设置的配置都保存在您用户主目录下的一个名为 `.gitconfig` 的文件中。

- 在 **Linux** 或 **macOS** 上，路径通常是 `~/.gitconfig`。
    
- 在 **Windows** 上，路径通常是 `C:\Users\<Your-Username>\.gitconfig`。
    

您可以直接编辑这个文件来修改您的全局配置，效果和使用 `git config` 命令是一样的。

### 总结

对于初次使用 Git 的用户，**最关键的步骤**就是设置 `user.name` 和 `user.email`。其他配置项可以根据您的使用习惯和需求逐步添加。

Bash

```
# 1. 必须的配置
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 2. 检查配置是否生效
git config --global --list

# 3. （推荐）设置新仓库的默认分支为 main
git config --global init.defaultBranch main
```

---

如果你设置错了全局配置，有几种方法可以修正或清除它们。我将从最常用、最安全的方法到最彻底的方法逐一介绍。

### 方法一：修改或覆盖错误的配置（最推荐）

这是最常见和最安全的方法。如果你只是某个配置项（比如邮箱）写错了，直接用正确的配置重新运行一遍命令即可，新的配置会自动覆盖旧的。

**示例：修改用户名**

假设你之前错误地设置了用户名： `git config --global user.name "Zahng San"` (拼写错误)

你只需要重新运行命令，输入正确的值：

Bash

```
git config --global user.name "Zhang San"
```

这样就完成了修改。修改邮箱或其他任何配置项也是同样的操作。

### 方法二：删除某一个全局配置项

如果你想删除某一个不再需要的配置项（比如一个不再使用的别名），而不是修改它，可以使用 `--unset` 选项。

**示例：删除一个别名**

假设你之前设置了一个别名 `git config --global alias.st status`，现在想删除它：

Bash

```
git config --global --unset alias.st
```

执行后，`alias.st` 这个配置项就会从你的全局配置中被移除。

**示例：删除用户名**

Bash

```
git config --global --unset user.name
```

> **注意**：删除 `user.name` 或 `user.email` 后，你在进行 `git commit` 时 Git 会提示你重新设置。

### 方法三：直接编辑配置文件（手动批量修改/删除）

所有的全局配置都存储在一个名为 `.gitconfig` 的文本文件中。你也可以直接用文本编辑器打开它进行修改或删除。

1. **找到 `.gitconfig` 文件：**
    
    - **Linux / macOS**: 在用户主目录下，路径是 `~/.gitconfig`
        
    - **Windows**: 在用户主目录下，路径是 `C:\Users\<你的用户名>\.gitconfig`
        
2. **打开并编辑：** 用任何文本编辑器（如 VS Code, Notepad++, Vim）打开这个文件。它的内容可能看起来像这样：
    
    Ini, TOML
    
    ```
    [user]
        name = Zhang San
        email = zhangsan@example.com
    [core]
        editor = code --wait
    [alias]
        st = status
        lg = log --oneline --graph --decorate --all
    ```
    
    你可以直接在这个文件里修改内容，或者删除你不需要的行（例如，删除 `[alias]` 下的所有行来清除所有别名），然后保存文件即可。
    

### 方法四：删除整个全局配置文件（彻底清除所有）

如果你想**完全清除所有全局配置**，恢复到 Git 刚安装时的状态，最直接的方法就是删除 `.gitconfig` 文件。

> **⚠️ 警告：这是一个彻底的操作，会删除你所有的全局配置，包括用户名、邮箱、别名、默认编辑器等。请谨慎使用。如果不确定，建议先备份该文件。**

1. **打开终端（Terminal / Git Bash / PowerShell）。**
    
2. **执行删除命令：**
    
    - **在 Linux / macOS 上：**
        
        Bash
        
        ```
        rm ~/.gitconfig
        ```
        
    - **在 Windows (PowerShell) 上：**
        
        Bash
        
        ```
        Remove-Item $env:USERPROFILE\.gitconfig
        ```
        
    - **在 Windows (CMD) 上：**
        
        Bash
        
        ```
        del %USERPROFILE%\.gitconfig
        ```
        

执行此命令后，`.gitconfig` 文件就被删除了。你可以通过 `git config --global --list` 来验证，此时应该会提示 `fatal: unable to read config file...` 或者没有任何输出，表示所有全局配置都已被清空。

之后，你需要重新设置最核心的用户名和邮箱：

Bash

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### 总结

|你的需求|推荐方法|命令/操作|
|---|---|---|
|**修改**一个错误的配置值|**方法一：覆盖**|`git config --global user.name "New Name"`|
|**删除**某一个配置项|**方法二：--unset**|`git config --global --unset alias.st`|
|批量修改或删除**部分**配置|**方法三：编辑文件**|打开 `~/.gitconfig` 文件手动编辑|
|**清除所有**全局配置，从头开始|**方法四：删除文件**|`rm ~/.gitconfig` (Linux/macOS)|

对于大多数“设置错了”的情况，**直接使用方法一重新运行命令来覆盖旧值是最简单和安全的方法。**

---

**现在已经不能直接使用 GitHub 密码来进行 `git push` 了**。

自从 2021 年 8 月起，为了安全，GitHub 停止了在 Git 操作中使用账户密码进行身份验证。无论你是用 Google 账号注册的还是用邮箱密码注册的，都必须使用新的、更安全的方式。

正确的做法是使用 **Personal Access Token (个人访问令牌，简称 PAT)** 来代替你的密码。

下面是详细的设置步骤，跟着做一遍即可解决问题。

### 总结：你需要做什么

1. 在 GitHub 网站上生成一个 Personal Access Token (PAT)。
    
2. 在 `git push` 时，终端提示输入密码（Password）时，**粘贴你刚刚生成的 PAT**。
    
3. （推荐）配置 Git Credential Helper，让电脑记住你的 PAT，以后就不用再输入了。
    
### 详细步骤

#### 第一步：在 GitHub 上生成 Personal Access Token (PAT)

1. 登录你的 [GitHub 账号](https://github.com/)。
    
2. 点击右上角的个人头像，然后选择 **Settings**。
    
3. 在左侧菜单栏滑到最下方，找到并点击 **Developer settings**。
    
4. 在左侧菜单栏，点击 **Personal access tokens**，然后选择 **Tokens (classic)**。 _(注：Fine-grained tokens 是更新、更精细的权限控制，但 Tokens (classic) 对初学者来说更简单直观)_
    
5. 点击 **Generate new token** 按钮，然后选择 **Generate new token (classic)**。
    
6. 现在你需要配置这个 Token：
    
    - **Note (备注)**: 给你的 Token起一个容易识别的名字，比如 `My Laptop Git` 或 `Windows-VSCode`，这样你就知道这个 Token 是用在哪里的。
        
    - **Expiration (有效期)**: 选择一个有效期。为了安全，建议选择 30天或 90天，到期后再重新生成。当然你也可以选择 "No expiration" (永不过期)，但不推荐。
        
    - **Select scopes (选择权限)**: 这是最重要的一步！你需要勾选此 Token 拥有的权限。对于 `git push` 到你的仓库，**只需要勾选 `repo` 这个大项即可**。它包含了所有对仓库进行操作的权限（push, pull, clone等）。
        
7. 滑动到页面最底部，点击 **Generate token** 按钮。
    

#### 第二步：复制并保存你的 Token

点击生成后，页面会显示一长串以 `ghp_` 开头的字符。这就是你的 Personal Access Token。

> **⚠️ 重要提示：** 这是**唯一一次**看到这个完整 Token 的机会！一旦你刷新或离开这个页面，就再也看不到了。 **请立即点击旁边的复制按钮，并将它粘贴到一个安全的地方**（比如你的密码管理器或一个临时文本文档中）。

#### 第三步：使用 Token 进行 `git push`

现在，回到你的终端（Terminal, Git Bash, CMD 等），再次运行 `git push` 命令。

当终端提示你输入用户名和密码时：

1. **Username for '[https://github.com](https://github.com/)':** 输入你的 **GitHub 用户名** (不是你的 Gmail 邮箱地址)。
    
2. **Password for 'https://<你的用户名>@github.com':** **在这里，粘贴你刚刚复制的那一长串 Personal Access Token (PAT)**。注意，输入时它可能不会显示出来，这是正常的安全机制。直接粘贴后按回车即可。
    

如果一切顺利，你的代码就会成功推送到 GitHub！

---

### 推荐操作：让电脑记住你的 Token

每次都输入这么长的 Token 很麻烦。你可以通过配置 Git 的凭证助手（Credential Helper）来让电脑自动记住它。在你成功用 PAT 推送一次之后，它就会被安全地保存起来。

只需要运行下面一条命令即可（根据你的操作系统选择）：

- **Windows:** (通常 Git for Windows 已默认配置好)
    
    Bash
    
    ```
    git config --global credential.helper manager-core
    ```
    
- **macOS:**
    
    Bash
    
    ```
    git config --global credential.helper osxkeychain
    ```
    
- **Linux:**
    
    Bash
    
    ```
    git config --global credential.helper cache
    # 这会将凭证在内存中缓存15分钟，你也可以配置更长时间
    # git config --global credential.helper 'cache --timeout=3600' # 缓存1小时
    ```
    

配置好之后，你只需要在第一次 `push` 时输入一次用户名和 PAT，后续再对同一个仓库操作时，Git 就会自动使用保存好的凭证，无需再次输入

---

将本地项目与远程仓库关联**

现在，我们将把前两天的学习成果用Git管理起来，并推送到GitHub。

1. **进入项目目录：** 在终端中，`cd` 到你的项目文件夹。
    
    Bash
    
    ```
    # 把下面的路径换成你自己的实际路径
    cd /Users/your_mac_username/PycharmProjects/Python_Learning_Path
    ```
    
2. **初始化本地仓库 (`git init`):**
    
    - 在项目文件夹根目录下，运行命令：`git init`
        
    - **作用：** 这个命令会在你的项目中创建一个隐藏的 `.git` 文件夹（储藏室），从此Git开始接管这个项目的版本控制。
        
3. **检查状态 (`git status`):**
    
    - 运行 `git status`。
        
    - **作用：** 这是你未来**最常用**的命令，它会告诉你当前工作区的状态。你会看到你的 `.py` 文件等显示为 "Untracked files" (未被追踪的文件)。
        
4. **添加到暂存区 (`git add`):**
    
    - 运行 `git add .` (注意 `add` 和 `.` 之间有空格)
        
    - **作用：** 这个命令告诉Git：“把当前目录下**所有**的修改（新增、改动）都放进那个‘待发货的包裹’（暂存区）里”。
        
5. **再次检查状态 (`git status`):**
    
    - 再次运行 `git status`。
        
    - 你会看到文件名都变成了绿色，并显示 "Changes to be committed" (等待提交的改动)。这证明它们已经成功进入暂存区。
        
6. **提交到本地仓库 (`git commit`):**
    
    - 运行 `git commit -m "Initial commit: Add day 1 and day 2 learning files"`
        
    - **作用：** `-m` 代表 "message"，这是给你的“存档点”添加的说明，**必须要有**，且要写得清晰。这个命令会把暂存区的内容正式存入你的本地仓库（储藏室）。
        
7. **关联远程仓库 (`git remote`):**
    
    - 回到你刚刚在GitHub创建的仓库页面，复制页面上 "…or push an existing repository from the command line" 下方的那两行或三行命令。
        
    - 第一行应该是 `git remote add origin https://github.com/你的用户名/Python_Learning_Path.git`
        
    - **在你的终端里，粘贴并运行这行命令。**
        
    - **作用：** 告诉本地Git，我们有一个远程仓库，它的昵称是 **`origin`**，地址是 `...`。
        
8. **（可选，但推荐）重命名主分支 (`git branch`):**
    
    - GitHub现在默认的主分支名叫 `main`。为了保持一致，运行：`git branch -M main`
        
9. **推送到远程仓库 (`git push`):**
    
    - 运行 `git push -u origin main`
        
    - **作用：** 把你本地仓库 `main` 分支上的所有提交，都推送到（上传到）昵称为 `origin` 的远程仓库。`-u`参数只需第一次使用，它会把本地的 `main` 和远程的 `main` 关联起来。
        
    - 此时可能会弹窗让你输入GitHub的用户名和密码（或者Token，根据你的设置）。
    - 2021年后，用户名和密码无法进行git push，只可用Token！！！
        

**验证成功：** 刷新你的GitHub仓库页面，你会惊喜地发现，你本地的所有代码文件都已经出现在网页上了！
