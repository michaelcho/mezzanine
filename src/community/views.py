from django.contrib.auth.models import User
from django.db import connection
from django.views.generic import TemplateView


class CommunityView(TemplateView):
    template_name = 'community.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CommunityView, self).get_context_data(*args, **kwargs)
        context['users'] = self.get_users()
        return context

    def query_users(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT\n" +
                "    `user`.`id`,\n"
                "    `user`.`username`,\n"
                "    `user`.`email`,\n"
                "    `user`.`is_staff`,\n"
                "    `user`.`is_active`,\n"
                "    `group`.`id`,\n"
                "    `group`.`name`\n"
                "FROM `auth_user_groups` AS `user_groups`\n" +
                "    INNER JOIN `auth_user` AS `user` ON (`user_groups`.`user_id` = `user`.`id`)\n" +
                "    INNER JOIN `auth_group` AS `group` ON (`user_groups`.`group_id` = `group`.`id`)\n" +
                "ORDER BY\n" +
                "    `user`.`id`,\n"
                "    `group`.`name` DESC;"
            )

            return cursor.fetchall()

    def get_users(self):
        result = self.query_users()
        output = []

        for row in result:
            record = None

            for item in output:
                if item['id'] == row[0]:
                    record = item
                    break

            if record is None:
                record = {
                    'id': row[0],
                    'username': row[1],
                    'email': row[2],
                    'is_staff': row[3] > 0,
                    'is_active': row[4] > 0,
                    'groups': []
                }
                output.append(record)

            record['groups'].append({
                'id': row[5],
                'name': row[6]
            })

        return output

community = CommunityView.as_view()
