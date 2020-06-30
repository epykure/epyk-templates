
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()


md = page.ui.rich.markdown()

page.ui.button("Refresh").click(
  md.build("""
# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------


Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```


```python
def function(value):
  print('Ok')
  return "Test"
```
""")
)