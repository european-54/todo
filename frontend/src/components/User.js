import React from 'react'

const UserItem = ({user}) => {
    user.last_name = undefined;
    user.first_name = undefined;
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}
