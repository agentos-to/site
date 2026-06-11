"""QR codes as text — the account protocol's challenge artifact.

One Unicode half-block string renders on every surface an agent lives on —
a terminal, a chat, the desktop act window — with no image pipeline.

    from agentos import qr

    artifact = qr.text(ref)   # → multi-line block, scan it with a phone
"""

import io

import qrcode


def text(payload: str) -> str:
    """Render `payload` as a scannable Unicode half-block QR.

    Low error-correction keeps the module count down — denser codes scan
    worse off a screen. `invert=True` matches light-on-dark terminals
    (the common agent surface); phone scanners decode either polarity.
    """
    code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=2,
    )
    code.add_data(payload)
    code.make(fit=True)
    out = io.StringIO()
    code.print_ascii(out=out, invert=True)
    return out.getvalue()
