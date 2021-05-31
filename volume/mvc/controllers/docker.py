import web

render = web.template.render("mvc/views/", base="template")

class Docker():

    def GET(self):
        try:
            return render.docker() # renderizando docker.html
        except Exception as e:
            return "Error " + str(e.args)