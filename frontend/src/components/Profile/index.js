import {
  List,
  ListItem,
  ListSubheader,
  TextField,
  Typography,
} from '@material-ui/core';
import axios from 'axios';
import React from 'react';
import AuthContext from '../../AuthContext';
import { url } from '../../utils/constants';
import { extractUId } from '../../utils/token';
import EditableFields from './EditableFields';

function Profile({ profile, ...props }) {
  const [profileDetails, setProfileDetails] = React.useState({});
  const token = React.useContext(AuthContext);
  const u_id = extractUId(token);
  React.useEffect(() => {
    axios
      .get(`/user/profile`, { params: { token, u_id } })
      .then(({ data }) => {
        console.log(data);
        setProfileDetails(data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, [profile, token]);

  function updateName(name_last, name_first) {
    axios
      .put(`/user/profile/setname`, { token, name_first, name_last })
      .then(() => {
        console.log('all good');
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function updateEmail(email) {
    axios
      .put(`/user/profile/setemail`, { token, email })
      .then(() => {
        console.log('all good');
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function updateHandle(handle) {
    axios
      .put(`/user/profile/sethandle`, { token, handle })
      .then(() => {
        console.log('all good');
      })
      .catch((err) => {
        console.error(err);
      });
  }

  const editable = u_id.toString() === profile;
  return (
    <>
      <Typography variant="h4">Profile</Typography>
      <List subheader={<ListSubheader>Profile Details</ListSubheader>}>
        <ListItem key={'name'}>
          <EditableFields
            editable={editable}
            masterValue={profileDetails.last_name}
            slaveValues={[profileDetails.first_name]}
            master={(passed_props) => (
              <TextField label={'Last Name'} {...passed_props} />
            )}
            slaves={[
              (passed_props) => (
                <TextField label={'First Name'} {...passed_props} />
              ),
            ]}
            onSave={updateName}
          />
        </ListItem>
        <ListItem key={'email'}>
          <EditableFields
            editable={editable}
            masterValue={profileDetails.email}
            master={(passed_props) => (
              <TextField label={'Email'} {...passed_props} />
            )}
            onSave={updateEmail}
          />
        </ListItem>
        <ListItem key={'handle'}>
          <EditableFields
            editable={editable}
            masterValue={'phlips'}
            master={(passed_props) => (
              <TextField label={'Handle'} {...passed_props} />
            )}
            onSave={updateHandle}
          />
        </ListItem>
      </List>
    </>
  );
}

export default Profile;
