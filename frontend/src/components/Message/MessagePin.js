import React from 'react';
import * as routecall from '../../utils/routecall';

import MdiIcon from '@mdi/react';
import { mdiPin, mdiPinOutline } from '@mdi/js';
import { IconButton } from '@material-ui/core';

import { url } from '../../utils/constants';

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
      routecall.post(`${url}/message/unpin`, {
        token,
        message_id,
      });
    } else {
      routecall.post(`${url}/message/pin`, {
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
