#!/bin/bash -x

set -e 
NAME='AmeliaPOS_Builder'
VER='0.1'
BUGURL='http://ameliapos.com/'

rm -rf $VER

# gather, createrepo, buildinstall
pungi --nosource --nosplitmedia --force \
    -c amelia-server-pungi.ks --name "$NAME" \
    --ver="$VER" --bugurl="$BUGURL" \
    -G -C -B

# now the contents for the ISO are at 
ISOBASE=$VER/i386/os

# Injeta KS, sobrescreve isolinux.cfg
cp amelia-server.ks $ISOBASE/
cp isolinux.cfg $ISOBASE/isolinux/

# Compila a iso
pungi --nosource --nosplitmedia --force \
    -c amelia-server-pungi.ks --name "$NAME" \
    --ver="$VER" --bugurl="$BUGURL" \
    -I

rm -fr "$ISOBASE/os" "$ISOBASE/debug"
echo ===============================
echo Imagens ISO em $VER/i386/iso
