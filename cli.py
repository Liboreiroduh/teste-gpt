"""Interface de linha de comando para o painel de LED."""

import argparse

from ledpanel.controller import LedPanelController


def main(argv=None):
    parser = argparse.ArgumentParser(description="Controle do Painel de LED")
    parser.add_argument("acao", choices=["ligar", "desligar", "mensagem"])
    parser.add_argument("--texto", help="Texto para atualizar no painel")
    args = parser.parse_args(argv)

    ctrl = LedPanelController()
    if args.acao == "ligar":
        ctrl.ligar()
    elif args.acao == "desligar":
        ctrl.desligar()
    elif args.acao == "mensagem":
        if not args.texto:
            parser.error("--texto eh obrigatorio para acao 'mensagem'")
        ctrl.atualizar_mensagem(args.texto)


if __name__ == "__main__":
    main()
