from flask import Blueprint, flash, redirect, render_template, request, url_for
from App.models.report import Report
from App.controllers.report import create_report, delete_report_by_id

# Create the blueprint
reports_views = Blueprint('reports_view', __name__)               #Configured views/report.py -Jaidi Akii-Bua
generate_views = Blueprint('generate_view', __name__)                   

@generate_views.route('/gen_report')
def view_generate_report():
    return render_template('admin/gen_reports.html')

@reports_views.route('/reports')
def view_reports():
    reports = Report.query.all()
    return render_template('admin/reports.html', reports=reports)

@reports_views.route('/report/<int:id>', methods=['GET'])
def view_report(id):
    # Fetch a specific report by ID
    report = Report.query.get(id)
    if not report:
        flash('Report not found!', 'error')
        return redirect(url_for('report_views.view_reports'))
    return render_template('report_detail.html', report=report)

@reports_views.route('/report/delete/<int:id>', methods=['POST'])
def delete_report(id):
    delete_report_by_id(id)
    flash('Report deleted successfully!', 'success')
    return redirect(url_for('report_views.view_reports'))

# Optional: Add a route to create a report if you need it in the view
@reports_views.route('/report/create', methods=['POST'])
def create_new_report():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)
    
    # Call your controller function to create a report
    new_report = create_report(file)
    flash('Report created successfully!', 'success')
    return redirect(url_for('report_views.view_reports'))