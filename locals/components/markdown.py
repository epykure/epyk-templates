
from epyk.core.Page import Report
from epyk.core.data import components


# Create a basic report object
page = Report()
page.headers.dev()


md = page.ui.rich.markdown('''
# H1
## H2
### value
#### rrr
##### H5
###### H6
value


''')
md.tooltips({"value": 'Ok'})

page.ui.button("Refresh").click(
  md.build(components.markdown("""
# H1
## H2
### H3
#### H4
##### value
###### H6

Alternatively, for H1 value H2, an underline-ish style:

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
  return "value"
```
""", {"value": 'Ok', 'youtube': 'test'}))
)


md2 = page.ui.rich.markdown('''
##### value
''')
md2.tooltips({"value": 'Ok2'})