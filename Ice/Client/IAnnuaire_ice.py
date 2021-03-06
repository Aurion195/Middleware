# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.2
#
# <auto-generated>
#
# Generated from file `IAnnuaire.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module server
_M_server = Ice.openModule('server')
__name__ = 'server'

if 'Annuaire' not in _M_server.__dict__:
    _M_server.Annuaire = Ice.createTempClass()
    class Annuaire(object):
        def __init__(self, id=0, nom='', numTel=''):
            self.id = id
            self.nom = nom
            self.numTel = numTel

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.id)
            _h = 5 * _h + Ice.getHash(self.nom)
            _h = 5 * _h + Ice.getHash(self.numTel)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_server.Annuaire):
                return NotImplemented
            else:
                if self.id is None or other.id is None:
                    if self.id != other.id:
                        return (-1 if self.id is None else 1)
                else:
                    if self.id < other.id:
                        return -1
                    elif self.id > other.id:
                        return 1
                if self.nom is None or other.nom is None:
                    if self.nom != other.nom:
                        return (-1 if self.nom is None else 1)
                else:
                    if self.nom < other.nom:
                        return -1
                    elif self.nom > other.nom:
                        return 1
                if self.numTel is None or other.numTel is None:
                    if self.numTel != other.numTel:
                        return (-1 if self.numTel is None else 1)
                else:
                    if self.numTel < other.numTel:
                        return -1
                    elif self.numTel > other.numTel:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_server._t_Annuaire)

        __repr__ = __str__

    _M_server._t_Annuaire = IcePy.defineStruct('::server::Annuaire', Annuaire, (), (
        ('id', (), IcePy._t_int),
        ('nom', (), IcePy._t_string),
        ('numTel', (), IcePy._t_string)
    ))

    _M_server.Annuaire = Annuaire
    del Annuaire

if '_t_liste' not in _M_server.__dict__:
    _M_server._t_liste = IcePy.defineSequence('::server::liste', (), _M_server._t_Annuaire)

_M_server._t_IAnnuaire = IcePy.defineValue('::server::IAnnuaire', Ice.Value, -1, (), False, True, None, ())

if 'IAnnuairePrx' not in _M_server.__dict__:
    _M_server.IAnnuairePrx = Ice.createTempClass()
    class IAnnuairePrx(Ice.ObjectPrx):

        def ajoutAnnuaire(self, nom, numTel, context=None):
            return _M_server.IAnnuaire._op_ajoutAnnuaire.invoke(self, ((nom, numTel), context))

        def ajoutAnnuaireAsync(self, nom, numTel, context=None):
            return _M_server.IAnnuaire._op_ajoutAnnuaire.invokeAsync(self, ((nom, numTel), context))

        def begin_ajoutAnnuaire(self, nom, numTel, _response=None, _ex=None, _sent=None, context=None):
            return _M_server.IAnnuaire._op_ajoutAnnuaire.begin(self, ((nom, numTel), _response, _ex, _sent, context))

        def end_ajoutAnnuaire(self, _r):
            return _M_server.IAnnuaire._op_ajoutAnnuaire.end(self, _r)

        def suppressionEnregistrement(self, id, context=None):
            return _M_server.IAnnuaire._op_suppressionEnregistrement.invoke(self, ((id, ), context))

        def suppressionEnregistrementAsync(self, id, context=None):
            return _M_server.IAnnuaire._op_suppressionEnregistrement.invokeAsync(self, ((id, ), context))

        def begin_suppressionEnregistrement(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_server.IAnnuaire._op_suppressionEnregistrement.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_suppressionEnregistrement(self, _r):
            return _M_server.IAnnuaire._op_suppressionEnregistrement.end(self, _r)

        def rechercherPersonne(self, nom, context=None):
            return _M_server.IAnnuaire._op_rechercherPersonne.invoke(self, ((nom, ), context))

        def rechercherPersonneAsync(self, nom, context=None):
            return _M_server.IAnnuaire._op_rechercherPersonne.invokeAsync(self, ((nom, ), context))

        def begin_rechercherPersonne(self, nom, _response=None, _ex=None, _sent=None, context=None):
            return _M_server.IAnnuaire._op_rechercherPersonne.begin(self, ((nom, ), _response, _ex, _sent, context))

        def end_rechercherPersonne(self, _r):
            return _M_server.IAnnuaire._op_rechercherPersonne.end(self, _r)

        def getListe(self, context=None):
            return _M_server.IAnnuaire._op_getListe.invoke(self, ((), context))

        def getListeAsync(self, context=None):
            return _M_server.IAnnuaire._op_getListe.invokeAsync(self, ((), context))

        def begin_getListe(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_server.IAnnuaire._op_getListe.begin(self, ((), _response, _ex, _sent, context))

        def end_getListe(self, _r):
            return _M_server.IAnnuaire._op_getListe.end(self, _r)

        def display(self, context=None):
            return _M_server.IAnnuaire._op_display.invoke(self, ((), context))

        def displayAsync(self, context=None):
            return _M_server.IAnnuaire._op_display.invokeAsync(self, ((), context))

        def begin_display(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_server.IAnnuaire._op_display.begin(self, ((), _response, _ex, _sent, context))

        def end_display(self, _r):
            return _M_server.IAnnuaire._op_display.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_server.IAnnuairePrx.ice_checkedCast(proxy, '::server::IAnnuaire', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_server.IAnnuairePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::server::IAnnuaire'
    _M_server._t_IAnnuairePrx = IcePy.defineProxy('::server::IAnnuaire', IAnnuairePrx)

    _M_server.IAnnuairePrx = IAnnuairePrx
    del IAnnuairePrx

    _M_server.IAnnuaire = Ice.createTempClass()
    class IAnnuaire(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::server::IAnnuaire')

        def ice_id(self, current=None):
            return '::server::IAnnuaire'

        @staticmethod
        def ice_staticId():
            return '::server::IAnnuaire'

        def ajoutAnnuaire(self, nom, numTel, current=None):
            raise NotImplementedError("servant method 'ajoutAnnuaire' not implemented")

        def suppressionEnregistrement(self, id, current=None):
            raise NotImplementedError("servant method 'suppressionEnregistrement' not implemented")

        def rechercherPersonne(self, nom, current=None):
            raise NotImplementedError("servant method 'rechercherPersonne' not implemented")

        def getListe(self, current=None):
            raise NotImplementedError("servant method 'getListe' not implemented")

        def display(self, current=None):
            raise NotImplementedError("servant method 'display' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_server._t_IAnnuaireDisp)

        __repr__ = __str__

    _M_server._t_IAnnuaireDisp = IcePy.defineClass('::server::IAnnuaire', IAnnuaire, (), None, ())
    IAnnuaire._ice_type = _M_server._t_IAnnuaireDisp

    IAnnuaire._op_ajoutAnnuaire = IcePy.Operation('ajoutAnnuaire', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_bool, False, 0), ())
    IAnnuaire._op_suppressionEnregistrement = IcePy.Operation('suppressionEnregistrement', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    IAnnuaire._op_rechercherPersonne = IcePy.Operation('rechercherPersonne', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_server._t_Annuaire, False, 0), ())
    IAnnuaire._op_getListe = IcePy.Operation('getListe', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_server._t_liste, False, 0), ())
    IAnnuaire._op_display = IcePy.Operation('display', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_server.IAnnuaire = IAnnuaire
    del IAnnuaire

# End of module server
