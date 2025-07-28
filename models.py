from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# ------------------------------
# DevOpsTool Model
# ------------------------------
class DevOpsTool(db.Model):
    __tablename__ = 'devops_tool'

    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    completion_percent = db.Column(db.Integer)  # Optional: store as integer percent

    # One-to-many relationship with PendingTopic
    pending_topics = db.relationship('PendingTopic', backref='devops_tool', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<DevOpsTool {self.tool_name} ({self.status})>"

# ------------------------------
# PendingTopic Model
# ------------------------------
class PendingTopic(db.Model):
    __tablename__ = 'pending_topic'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey('devops_tool.id'), nullable=False)

    def __repr__(self):
        return f"<PendingTopic {self.topic} (Tool ID: {self.tool_id})>"

