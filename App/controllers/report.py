from App.models.report import Report
from App.database import db

def create_report(file):
    new_report = Report(file)
    db.session.add(new_report)
    db.session.commit()
    return new_report

def delete_report_by_id(id):
    report = Report.query.get(id)
    if not report:
      print(f'Report {id} not found!')
      return
    report.remove_file(report.filename)
    db.session.delete(report)
    db.session.commit()
    print(f'Report {id} deleted')

def delete_report_by_filename(filename):
    report = Report.query.filter_by(filename=filename).first()
    if not report:
      print(f'Report {filename} not found!')
      return
    report.remove_file(report.filename)
    db.session.delete(report)
    db.session.commit()
    print(f'Report {filename} deleted')
