import React from 'react'
import React from 'react'



const UserItem = ({user}) => {
    user.first_name = undefined;
    user.last_name = undefined;
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


const UserList = ({users}) => {
   return (
       <table>
           <th>
               Username
           </th>
           <th>
               Firs_name
           </th>
           <th>
               Last_name
           </th>
           <th>
               Email
           </th>
           {users.map((user) => <UserItem user={user} />)}
       </table>
   )
}


export default UserList
