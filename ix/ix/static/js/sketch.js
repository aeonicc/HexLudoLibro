let sketch = function(p)
{
p.setup = function(){
p.createCanvas(100, 100);
}
p.draw = function(){
p.background(0);
}
};
new p5(sketch, 'container');