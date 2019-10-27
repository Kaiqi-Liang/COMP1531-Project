import React from 'react';
import axios from 'axios';

import MdiIcon from '@mdi/react';
import { mdiPin, mdiPinOutline } from '@mdi/js';
import { IconButton } from '@material-ui/core';

import { withTheme } from '@material-ui/styles';
import AuthContext from '../../AuthContext';

function MessagePin({
  message_id,
  is_pinned = false,
  theme,
}) {

  const [isPinned, setIsPinned] = React.useState(is_pinned);
  React.useEffect(() => setIsPinned(is_pinned),[is_pinned]);

  const token = React.useContext(AuthContext);

  const toggle = () => {
    if (isPinned) {
      axios.post(`/message/unpin`, {
        token,
        message_id,
      });
    } else {
      axios.post(`/message/pin`, {
        token,
        message_id,
      });
    }
    // Optimistic re-rendering
    // setIsPinned(isPinned => !!!isPinned);
  };

  return (
    <IconButton
    onClick={toggle}
    style={{ margin: 1 }}
    size="small"
    edge="end"
    aria-label="delete"
    >
    {isPinned ? (
        <MdiIcon
        path={mdiPin}
        size="1em"
        color={theme && theme.palette.action.active}
        />
    ) : (
        <MdiIcon
        path={mdiPinOutline}
        size="1em"
        color={theme && theme.palette.action.active}
        />
    )}
    </IconButton>
  );
}

export default withTheme(MessagePin);
