
import { useState } from 'react';
import RegisterClinician from './RegisterClinician';
import AuthenticateClinician from './AuthenticateClinician';

export default function LogIn() {
    return (
        <div>
            <AuthenticateClinician/>
            <RegisterClinician/>
        </div>
    )
}
