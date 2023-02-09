def format_list_student(students):
    string = '''<table>
                    <thead>
                        <tr>
                            <th>First name</th>
                            <th>Last name</th>
                            <th>Email</th>
                            <th>Birthday</th>
                            <th>Phone</th>
                            <th>City</th>
                            <th>Update</th>
                        </tr>
                    <thead>
                <tbody>'''
    for st in students:
        string += f'''<tr>
                        <td>{st.first_name}</td>
                        <td>{st.last_name}</td>
                        <td>{st.email}</td>
                        <td>{st.birthday}</td>
                        <td>{st.phone}</td>
                        <td>{st.city if st.city else ''}</td>
                        <td><a href="/students/update/{st.pk}/">Edit</a></td>
                    </tr>'''
    string += '</tbody></table>'
    return string
