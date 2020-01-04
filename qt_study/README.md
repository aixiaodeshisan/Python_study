# QtStudy

## ui部件常见流程
```Cython
# 创建应用
app = QApplication(sys.argv)

# 创建窗体，开始布局
ex = Example()
ex.initUi()

# 监听应用，最终关闭
sys.exit(app.exec_())
```