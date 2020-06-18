# DeathX_py
print("helloworld")
# feature-A test
在不同分支下，就算查看本地文件都不会一样，在不同分支下本地文件也会随之改变。
# git 操作
<<<<<<< HEAD

`git add` 添加至暂存区  

`git commit` 提交到仓库

`git commit -am` 合并add与commit操作

`git log` 只能查看以当前状态为终点的历史日志。所以这里要使用git 

`git log --graph` 查看分支树

`git reflog` 查看当前仓库的操作日志。

`git branch` 查看当前分支

`git checkout -b xxx` 创建新分支xxx

`git checkout - `最近使用分支与master切换

`git merge --no-ff xxx` 将xxx分支合并到master

`git reset --hard ***` 回溯到指定时间点，***为该时间点的希哈值，在git log中查看历史节点，在git reflog查看未来节点
=======
`git add` 添加至暂存区  

'git commit' 提交到仓库

'git commit -am xxx' 合并add与commit操作

'git log' 只能查看以当前状态为终点的历史日志。所以这里要使用git 

'git log --graph' 查看分支树

'git reflog' 查看当前仓库的操作日志。

'git branch' 查看当前分支

'git checkout -b xxx' 创建新分支xxx

'git checkout -' 最近使用分支与master切换

'git merge --no-ff xxx' 将xxx分支合并到master

'git reset --hard ***' 回溯到指定时间点，***为该时间点的希哈值，在git log中查看历史节点，在git reflog查看未来节点
>>>>>>> 6f85b95ec9886569789bdfe77037bf3f94a04e52


