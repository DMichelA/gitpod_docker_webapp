import web

render = web.template.render("mvc/views/", base="template")

class Ubuntu():

    def GET(self):
        try:
            return render.ubuntu() # renderizando ubuntu.html
        except Exception as e:
            return "Error " + str(e.args)