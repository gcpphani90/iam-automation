locals {
  json_data_7 = jsondecode(file("./users.json"))
}

locals {

  helper_list = flatten([ for v in local.json_data_7.user_roles: 
            [ for project, role in v:
            [ for roles, users in role:
            [ for i in users:
             { "project" = project
               "role" = roles
                "member" = i}
            ]
            ]
            ]
          ])
}

resource "google_project_iam_member" "rolebinding" {
  for_each     = {for idx, v in local.helper_list: idx => v }
  project = each.value.project
  role    = "roles/${each.value.role}"
  member  = each.value.member
}
