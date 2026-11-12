from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
        <h1>Bienvenidos a mi proyecto Django</h1>
        <p>Mi primera aplicación web con Django.</p>
    """)