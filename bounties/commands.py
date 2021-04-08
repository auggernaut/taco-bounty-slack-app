from flask import jsonify
from utils import block
from storage import payup, bounties


def payup_command(request):
    data = request.form
    team_id, user_id, text = data['team_id'], data['user_id'], data['text']
    payup(team_id, user_id, text)
    return "payuped: `{}`".format(text)


def bounties_command(request):
    data = request.form
    team_id, user_id, text = data['team_id'], data['user_id'], data['text']
    items = bounties(team_id, user_id, text)
    items_text = "\n".join(["%s. %s" % (i, x) for i, x in enumerate(items, 1)])

    block_args = [
        ('mrkdwn', "bountiesing `{}`".format(text)),
        ('divider',),
        ('mrkdwn', items_text),
        ('divider',),
        ('mrkdwn', "_Trying filtering by tag and date_ `/bounties last 7 days #mgmt`."),
        ('mrkdwn', "_Share your response with the room by adding `public` anywhere in your response_"),
    ]
    resp = {
        "text": items_text,
        "response_type": "in_channel" if "public" in text else "ephemeral",
        "blocks": [block(*args) for args in block_args]
    }
    return jsonify(resp)
