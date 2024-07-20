@app.route('/distract')
def distract():
    if request.method == "POST":
        global img
        ex = ['static/cobra.png', 'static/downwarddog.png', 'static/halfbend.png', 'static/mountain.png', 'static/plank.png', 'static/seatbend.png', 'static/staff.png', 'static/warrior1.png']
        img = random.choice(ex)
        return render_template('/distractions.html', img = img), 200, {'Cache-Control': 'no-cache, no-store, must-revalidate'}
    else:
        return render_template('/distractions_start.html')