from django.shortcuts import render
from django.db import connection
from .forms import LgaForm

def polling_unit_results(request, polling_unit_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = %s", [polling_unit_id])
        results = cursor.fetchone()

    return render(request, 'election_app/polling_unit_results.html', {'results': results})


def lga_results(request):
    lgas = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM lga")
        lgas = cursor.fetchall()

    if request.method == 'POST':
        lga_id = request.POST['lga']
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT party_abbreviation, SUM(party_score) FROM announced_pu_results WHERE lga_name = (SELECT lga_name FROM lga WHERE lga_id = %s) GROUP BY party_abbreviation", [lga_id])
            results = cursor.fetchall()

        return render(request, 'election_app/lga_results.html', {'lgas': lgas, 'results': results, 'selected_lga': lga_id})

    return render(request, 'election_app/lga_results.html', {'lgas': lgas})
