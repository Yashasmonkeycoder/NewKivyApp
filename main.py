import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.animation import Animation

Builder.load_string('''
<updlbl>:
    size:500,1000
    canvas.before: 
        Color: 
            rgba: (1, 1, 1, 1) 
        Rectangle: 
            source:'background.png'
            size: root.width, root.height 
            pos: self.pos
    Label:
        id: updlbl
        text: '[b]Output[/b]:'
		font_size:"25sp"
		pos_hint:{"x":-0.3,"y":-0.03}
		color: "5d18d6"
		markup: True
	Label:
    	text:"Rgb/Hex converter"
    	pos_hint:{"y":0.46}
    	background_color: "3d3d3d"
    	font_size:"25sp"
	Label:
		text:"this is a small app by yashas :-)"
		font_size:"8sp"
	    color:(1,1,1,1)
 	   pos_hint:{"x":0,"y":-0.4}
	TextInput: 
        id: input
        hint_text:'Enter hex/rgb code:'
        pos_hint: {'x': 0.1, 'y': 0.8} 
        font_size: "20sp"
        size_hint: 0.8, 0.09
        padding: 40
    Label:
    	text:"hex format: xxxxxx   and   rgb format: xxx,xxx,xxx"
    	font_size:"10sp"
    	pos_hint:{"y":.27}
    Button:
        text: 'Convert'
		size_hint:.4,.08
		pos_hint:{"x":0.28,"y":0.6}
		border:1,1,1,1
		on_press:root.convert()
	TextInput: 
        id: output
        hint_text:'Output will be shown here'
        pos_hint: {'x': 0.1, 'y': 0.3}
        font_size: "20sp"
        size_hint: 0.8, 0.09
        padding: 40
 ''')

class updlbl(RelativeLayout):
     def __init__(self, **kwargs):
       super(updlbl,self).__init__(**kwargs)
       pass
     def ch_text(self, txxt):
     	       self.ids.updlbl.text=txxt
     	       anim = Animation(x=50, size=(80, 80), t='in_quad')
     	       anim += Animation(x=-50,size=(40, 40), t='in_quad')
     	       anim.repeat=True
     	       anim.start(self.ids.updlbl)
     def toHEX(self,sett):
     		try:
     			val = sett.split(",")
     			conv = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g"}
     			t1 = str(float(val[0])/16).split(".")
     			v1 = conv[int(t1[0])]
     			v2 = conv[int(float("0."+t1[1])*16)]
     			t2 = str(float(val[1])/16).split(".")
     			v3 = conv[int(t2[0])]
     			v4 = conv[int(float("0."+t2[1])*16)]
     			t3 = str(float(val[2])/16).split(".")
     			v5 = conv[int(t3[0])]
     			v6 = conv[int(float("0."+t3[1])*16)]
     			self.ids.output.text = f" #{v1}{v2}{v3}{v4}{v5}{v6}"
     		except:
     			self.ids.output.text = "Something is not correct, \ncheck again example of rgb code: 200,20,60"
     def toRGB(self,sett):
     		conv = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g"}
     		try:
     			conv2 = {str(v): k for k, v in conv.items()}
     			h1 = []
     			for bb in sett:
     				h1.append(bb)
     			n1 = (int(conv2[h1[0]])*16)+(int(conv2[h1[1]]))
     			n2 = (int(conv2[h1[2]])*16)+(int(conv2[h1[3]]))
     			n3 = (int(conv2[h1[4]])*16)+(int(conv2[h1[5]]))
     			hk = f"rgb({n1},{n2},{n3})"
     			self.ids.output.text = hk
     		except:
     			self.ids.output.text = "something is not correct, \nplease enter in small letters and try. error:HEX"
     			
     def convert(self):
     	code = "HEX"
     	sett = self.ids.input.text
     	for x in sett:
     		if x == ',':
     			code = "RGB"
     		if code == "RGB":
     			self.toHEX(sett)
     		elif code == "HEX":
     			self.toRGB(sett)
     		else:
     			self.ids.output.text = "oh no! something went wrong"
	  
class UpdateLabel(App):
     def build(self):
     	self.title = "Update Label"
     	return updlbl()

if __name__ == '__main__':
    UpdateLabel().run()
