

if __name__ == "__main__":

    className = "Duty"

    rpcClientModel = """package com.bozhong.nursetransfer.service;

import com.bozhong.nursetransfer.common.dto.resp.{className}RespDTO;
import com.bozhong.nursetransfer.core.Result;
import java.util.List;
import java.util.Map;
import lombok.Setter;

/**
 * @author 徐顺洁
 * @date 2024年08月15日 14:22:26
 */
@Setter
public class {className}ReadServiceRPCClient implements {className}ReadServiceRPC {open}

    private {className}ReadServiceRPC {classLowerName}ReadServiceRPC;
    
    @Override
    public Result<List<{className}RespDTO>> listByWhere(Map<String, Object> params) {open}
        return {classLowerName}ReadServiceRPC.listByWhere(params);
    {close}

{close}""".format(className=className, classLowerName=className[0].lower()+className[1:], open="{", close="}")
    with open(f"{className}ReadServiceRPCClient.java", "w", encoding='utf-8') as f:
        f.write(rpcClientModel)