# --coding:utf-8--
print u"开始练习"
print "-----------"
name = 'Zed A. Shaw'
age = 35  # not lie
heght = 74  # inches
weight = 180  # lbs
eyes = "blue"
teeth = "white"
hair = "Brown"

print "Let's talk about %r." % name
print "He's %r inches tall." % heght
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."

print "He's got %r eyss an %r hair." % (eyes, hair)

print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, heght, weight, age + heght + weight)
