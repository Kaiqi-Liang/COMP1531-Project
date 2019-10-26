import React from "react";
import axios from 'axios';
import {
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
  DialogContentText,
  Button,
  TextField,
  Grid,
  FormControlLabel,
  RadioGroup,
  Radio,
} from "@material-ui/core";
import AuthContext from "../../AuthContext";
import { PERMISSION_IDS } from "../../utils/constants";

function SetUserPermissionsDialog({ children, ...props }) {

    const [open, setOpen] = React.useState(false);
    const [permissionId, setPermissionId] = React.useState(PERMISSION_IDS.MEMBER);

    const token = React.useContext(AuthContext);

    const handleRadioChange = event => {
        const newPermissionId = parseInt(event.target.value,10);
        setPermissionId(newPermissionId);
    };

    function handleClickOpen() {
        setOpen(true);
    }

    function handleClose() {
        setOpen(false);
    }

    function handleSubmit(event) {
        event.preventDefault();

        if (!event.target[0].value) return;

        const u_id = parseInt(event.target[0].value,10);
        const permission_id = parseInt(permissionId,10);

        axios
        .post(`/admin/userpermission/change`, { token, u_id, permission_id })
        .then(response => {
            console.log(response);
        })
        .catch(err => {});
    }

    return <>
        <div onClick={handleClickOpen}>
        {children}
        </div>
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
        >
            <DialogTitle id="form-dialog-title">Set User Permissions</DialogTitle>
            <form onSubmit={handleSubmit}>
                <DialogContent>
                    <DialogContentText>
                    Enter a user id below to set permissions for this user
                    </DialogContentText>
                    <Grid
                        container
                        spacing={2}
                        direction="row"
                        justify="center"
                        alignItems="center"
                    >
                        <Grid item xs={12}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="u_id"
                                label="User ID"
                                name="u_id"
                                fullWidth
                            />
                        </Grid>
                        <Grid container item justify="center" alignItems="center">
                            <RadioGroup aria-label="position" name="position" value={permissionId} onChange={handleRadioChange} row>
                                <FormControlLabel
                                    value={PERMISSION_IDS.MEMBER}
                                    control={<Radio color="primary" />}
                                    label="Member"
                                    labelPlacement="bottom"
                                />
                                <FormControlLabel
                                    value={PERMISSION_IDS.ADMIN}
                                    control={<Radio color="primary" />}
                                    label="Admin"
                                    labelPlacement="bottom"
                                />
                                <FormControlLabel
                                    value={PERMISSION_IDS.OWNER}
                                    control={<Radio color="primary" />}
                                    label="Owner"
                                    labelPlacement="bottom"
                                />
                            </RadioGroup>
                        </Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                    Cancel
                    </Button>
                    <Button onClick={handleClose} type="submit" color="primary">
                    Set
                    </Button>
                </DialogActions>
            </form>
        </Dialog>
    </>;
}

export default SetUserPermissionsDialog;
